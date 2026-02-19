const MAX_FILE_SIZE_BYTES = 5 * 1024 * 1024;

export function validateAnalyzeInput(file, drugNamesRaw) {
  if (!file) {
    return { valid: false, statusCode: 400, message: 'VCF file is required.' };
  }

  if (file.size > MAX_FILE_SIZE_BYTES) {
    return { valid: false, statusCode: 400, message: 'VCF file must be 5MB or smaller.' };
  }

  const drugs = String(drugNamesRaw || '')
    .split(',')
    .map((drug) => drug.trim())
    .filter(Boolean)
    .map((drug) => drug.toUpperCase());

  if (drugs.length === 0) {
    return { valid: false, statusCode: 400, message: 'At least one drug name is required.' };
  }

  return { valid: true, drugs };
}

export { MAX_FILE_SIZE_BYTES };
