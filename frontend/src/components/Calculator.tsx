import { useState } from 'react';
import { calculate } from '../services/api';

const Calculator: React.FC = () => {
  const [a, setA] = useState<string>('');
  const [b, setB] = useState<string>('');
  const [operation, setOperation] = useState<string>('add');
  const [result, setResult] = useState<number | null>(null);
  const [error, setError] = useState<string | null>(null);
  const [loading, setLoading] = useState<boolean>(false);

  const handleCalculate = async () => {
    setError(null);
    setResult(null);
    
    // Validate inputs
    const aNum = parseFloat(a);
    const bNum = parseFloat(b);
    
    if (isNaN(aNum) || isNaN(bNum)) {
      setError('Please enter valid numbers for both operands');
      return;
    }

    try {
      setLoading(true);
      const response = await calculate(aNum, bNum, operation);
      setResult(response);
    } catch (err) {
      setError(err instanceof Error ? err.message : 'An unexpected error occurred');
    } finally {
      setLoading(false);
    }
  };

  const handleReset = () => {
    setA('');
    setB('');
    setOperation('add');
    setResult(null);
    setError(null);
  };

  return (
    <div style={{ maxWidth: '400px', margin: '2rem auto', padding: '1rem' }}>
      <h2>Calculator</h2>
      
      <div style={{ marginBottom: '1rem' }}>
        <label htmlFor="a">First number:</label><br />
        <input
          id="a"
          type="number"
          step="any"
          value={a}
          onChange={(e) => setA(e.target.value)}
          placeholder="Enter first number"
          style={{ width: '100%', padding: '0.5rem', marginTop: '0.25rem' }}
        />
      </div>

      <div style={{ marginBottom: '1rem' }}>
        <label htmlFor="b">Second number:</label><br />
        <input
          id="b"
          type="number"
          step="any"
          value={b}
          onChange={(e) => setB(e.target.value)}
          placeholder="Enter second number"
          style={{ width: '100%', padding: '0.5rem', marginTop: '0.25rem' }}
        />
      </div>

      <div style={{ marginBottom: '1rem' }}>
        <label htmlFor="operation">Operation:</label><br />
        <select
          id="operation"
          value={operation}
          onChange={(e) => setOperation(e.target.value)}
          style={{ width: '100%', padding: '0.5rem', marginTop: '0.25rem' }}
        >
          <option value="add">Add</option>
          <option value="subtract">Subtract</option>
          <option value="multiply">Multiply</option>
          <option value="divide">Divide</option>
        </select>
      </div>

      <div style={{ display: 'flex', gap: '0.5rem', marginBottom: '1rem' }}>
        <button 
          onClick={handleCalculate} 
          disabled={loading}
          style={{ 
            flex: 1, 
            padding: '0.75rem', 
            backgroundColor: loading ? '#ccc' : '#007bff',
            color: 'white',
            border: 'none',
            borderRadius: '4px',
            cursor: loading ? 'not-allowed' : 'pointer'
          }}
        >
          {loading ? 'Calculating...' : 'Calculate'}
        </button>
        <button 
          onClick={handleReset} 
          disabled={loading}
          style={{ 
            padding: '0.75rem', 
            backgroundColor: '#6c757d',
            color: 'white',
            border: 'none',
            borderRadius: '4px',
            cursor: 'pointer'
          }}
        >
          Reset
        </button>
      </div>

      {error && (
        <div 
          data-testid="calc-error"
          style={{ 
            color: 'red', 
            backgroundColor: '#f8d7da',
            border: '1px solid #f5c6cb',
            padding: '0.75rem',
            borderRadius: '4px',
            marginTop: '0.5rem'
          }}
        >
          {error}
        </div>
      )}

      {result !== null && (
        <div style={{ 
          backgroundColor: '#d4edda',
          border: '1px solid #c3e6cb',
          padding: '0.75rem',
          borderRadius: '4px',
          marginTop: '0.5rem'
        }}>
          <strong>Result:</strong> {result}
        </div>
      )}
    </div>
  );
};

export default Calculator;
