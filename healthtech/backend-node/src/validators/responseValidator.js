export function validatePythonResponse(payload) {
  if (!payload || typeof payload !== 'object') {
    return { valid: false, message: 'Invalid response from pharmacogenomics engine.' };
  }

  const requiredKeys = [
    'patient_summary',
    'matched_variants',
    'drug_recommendations',
    'confidence',
    'explanation',
    'disclaimer'
  ];

  const missingKeys = requiredKeys.filter((key) => !(key in payload));
  if (missingKeys.length > 0) {
    return {
      valid: false,
      message: `Python response is missing keys: ${missingKeys.join(', ')}`
    };
  }

  return { valid: true };
}
