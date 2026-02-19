import { useState } from 'react';
import { analyzePgx } from './api';
import './styles.css';

export default function App() {
  const [vcfFile, setVcfFile] = useState(null);
  const [drugNames, setDrugNames] = useState('CODEINE,WARFARIN');
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');
  const [result, setResult] = useState(null);

  async function handleSubmit(event) {
    event.preventDefault();
    setError('');
    setResult(null);

    if (!vcfFile) {
      setError('Please select a VCF file.');
      return;
    }

    if (!drugNames.trim()) {
      setError('Please provide at least one drug name.');
      return;
    }

    setLoading(true);
    try {
      const data = await analyzePgx({ vcfFile, drugNames });
      setResult(data);
    } catch (submitError) {
      setError(submitError.message);
    } finally {
      setLoading(false);
    }
  }

  return (
    <main className="container">
      <h1>AI-Assisted Pharmacogenomic Decision Support</h1>
      <p className="subtitle">Upload VCF (v4.2) and requested drugs. Frontend calls Node.js API Gateway only.</p>

      <form className="card" onSubmit={handleSubmit}>
        <label>
          VCF file
          <input
            type="file"
            accept=".vcf,text/plain"
            onChange={(event) => setVcfFile(event.target.files?.[0] || null)}
          />
        </label>

        <label>
          Drug names (comma-separated)
          <input
            type="text"
            value={drugNames}
            onChange={(event) => setDrugNames(event.target.value)}
            placeholder="CODEINE,WARFARIN"
          />
        </label>

        <button disabled={loading} type="submit">
          {loading ? 'Analyzing...' : 'Analyze'}
        </button>
      </form>

      {error ? <p className="error">{error}</p> : null}

      {result ? (
        <section className="card">
          <h2>Analysis Result</h2>
          <pre>{JSON.stringify(result, null, 2)}</pre>
        </section>
      ) : null}
    </main>
  );
}
