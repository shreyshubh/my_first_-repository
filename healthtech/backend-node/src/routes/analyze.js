import express from 'express';
import multer from 'multer';
import { analyzeWithPython } from '../services/pythonService.js';
import { validateAnalyzeInput, MAX_FILE_SIZE_BYTES } from '../validators/inputValidator.js';
import { validatePythonResponse } from '../validators/responseValidator.js';

const router = express.Router();

const upload = multer({
  storage: multer.memoryStorage(),
  limits: { fileSize: MAX_FILE_SIZE_BYTES }
});

router.post('/', upload.single('vcf_file'), async (req, res) => {
  const validation = validateAnalyzeInput(req.file, req.body.drug_names);
  if (!validation.valid) {
    return res.status(validation.statusCode).json({ error: validation.message });
  }

  try {
    const vcfText = req.file.buffer.toString('utf-8');
    const payload = {
      vcf_text: vcfText,
      drugs: validation.drugs
    };

    const pythonResponse = await analyzeWithPython(payload);
    const responseValidation = validatePythonResponse(pythonResponse);

    if (!responseValidation.valid) {
      return res.status(502).json({ error: responseValidation.message });
    }

    return res.status(200).json(pythonResponse);
  } catch (error) {
    if (error.code === 'LIMIT_FILE_SIZE') {
      return res.status(400).json({ error: 'VCF file must be 5MB or smaller.' });
    }

    if (error.response) {
      return res.status(error.response.status || 502).json(error.response.data);
    }

    return res.status(502).json({
      error: 'Unable to reach pharmacogenomics engine.',
      details: error.message
    });
  }
});

export default router;
