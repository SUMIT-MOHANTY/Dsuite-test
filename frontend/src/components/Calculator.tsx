import React, { useState } from 'react';
import { calculate } from '../services/api';

type Operation = 'add' | 'subtract' | 'multiply' | 'divide';

const Calculator: React.FC = () => {
  const [a, setA] = useState<string>('');
  const [b, setB] = useState<string>('');
  const [operation, setOperation] = useState<Operation>('add');
  const [result, setResult] = useState<number | null>(null);
  const [error, setError] = useState<string | null>(null);

  const handleCalculate = async () => {
    setError(null);
    setResult(null);

    try {
      const numA = parseFloat(a);
      const numB = parseFloat(b);

      if (isNaN(numA) || isNaN(numB)) {
        setError('Please enter valid numbers');
        return;
      }

      const res = await calculate(numA, numB, operation);
      setResult(res);
    } catch (err) {
      setError(err instanceof Error ? err.message : 'An error occurred');
    }
  };

  return (
    <div>
      <h2>Calculator</h2>
      <div>
        <input
          type="number"
          value={a}
          onChange={(e) => setA(e.target.value)}
          placeholder="First number"
        />
        <select
          value={operation}
          onChange={(e) => setOperation(e.target.value as Operation)}
        >
          <option value="add">+</option>
          <option value="subtract">-</option>
          <option value="multiply">×</option>
          <option value="divide">÷</option>
        </select>
        <input
          type="number"
          value={b}
          onChange={(e) => setB(e.target.value)}
          placeholder="Second number"
        />
        = <span>{result ?? '?'}</span>
      </div>
      <button onClick={handleCalculate}>Calculate</button>
      {error && <p style={{ color: 'red' }}>{error}</p>}
    </div>
  );
};

export default Calculator;
