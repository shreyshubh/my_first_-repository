const NODE_API_URL = import.meta.env.VITE_NODE_API_URL || 'http://localhost:3000';

export async function analyzePgx({ vcfFile, drugNames }) {
  const formData = new FormData();
  formData.append('vcf_file', vcfFile);
  formData.append('drug_names', drugNames);

  const response = await fetch(`${NODE_API_URL}/analyze`, {
    method: 'POST',
    body: formData
  });

  const payload = await response.json();
  if (!response.ok) {
    throw new Error(payload.error || 'Analysis request failed.');
  }

  return payload;
}
