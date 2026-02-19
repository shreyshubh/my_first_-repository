import express from 'express';
import analyzeRouter from './routes/analyze.js';

const app = express();
const PORT = process.env.PORT || 3000;

app.get('/health', (_req, res) => {
  res.status(200).json({ status: 'ok' });
});

app.use('/analyze', analyzeRouter);

app.use((err, _req, res, _next) => {
  if (err?.code === 'LIMIT_FILE_SIZE') {
    return res.status(400).json({ error: 'VCF file must be 5MB or smaller.' });
  }

  return res.status(500).json({ error: 'Internal server error.' });
});

app.listen(PORT, () => {
  console.log(`Node API Gateway running on port ${PORT}`);
});
