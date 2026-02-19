import axios from 'axios';

const PYTHON_BASE_URL = process.env.PYTHON_BASE_URL || 'http://127.0.0.1:8000';

export async function analyzeWithPython(payload) {
  const response = await axios.post(`${PYTHON_BASE_URL}/analyze`, payload, {
    timeout: 15000,
    headers: { 'Content-Type': 'application/json' }
  });

  return response.data;
}
