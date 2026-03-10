import React, { useState } from 'react';
import { calculate } from '../services/api';

export const Calculator: React.FC = () => {
  const [a, setA] = useState<number>(0);
  const [b, setB] = useState<number>(0);
  const [operation, setOperation] = useState<'add' | 'subtract' | 'multiply' | 'divide'>('add');
  const [result, setResult] = useState<number | null>(null);
  const [error, setError] = useState<string | null>(null);

  const handleCalculate = async () => {
    setError(null);
    try {
      const response = await calculate({ a, b, operation });
      setResult(response.result);
    } catch (err) {
      setError((err as Error).message);
      setResult(null);
    }
  };

  return (
    <div className="calculator">
      <h2>Calculator</h2>
      <div>
        <input 
          type="number" 
          value={a} 
          onChange={(e) => setA(parseFloat(e.target.value))} 
          placeholder="First number"
        />
        <select 
          value={operation} 
          onChange={(e) => setOperation(e.target.value as any)}
        >
          <option value="add">+</option>
          <option value="subtract">-</option>
          <option value="multiply">×</option>
          <option value="divide">÷</option>
        </select>
        <input 
          type="number" 
          value={b} 
          onChange={(e) => setB(parseFloat(e.target.value))} 
          placeholder="Second number"
        />
        <button onClick={handleCalculate}>=</button>
      </div>
      {result !== null && <div className="result">Result: {result}</div>}
      {error && <div className="error">Error: {error}</div>}
    </div>
  );
};
