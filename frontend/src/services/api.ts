export interface CalculateParams {
  a: number;
  b: number;
  operation: 'add' | 'subtract' | 'multiply' | 'divide';
}

export interface CalculateResult {
  result: number;
}

export interface CalculateError {
  error: string;
}

export async function calculate(params: CalculateParams): Promise<CalculateResult> {
  const response = await fetch('/api/v1/calculate', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(params)
  });
  
  if (!response.ok) {
    const error: CalculateError = await response.json();
    throw new Error(error.error || 'Calculation failed');
  }
  
  return await response.json();
}
