const API_BASE_URL = import.meta.env.VITE_API_URL || 'http://localhost:5000/api/v1';

type Operation = 'add' | 'subtract' | 'multiply' | 'divide';

interface CalculateRequest {
  a: number;
  b: number;
  operation: Operation;
}

interface CalculateResponse {
  result: number;
}

interface ErrorResponse {
  error: string;
}

export async function calculate(
  a: number,
  b: number,
  operation: Operation
): Promise<number> {
  const response = await fetch(`${API_BASE_URL}/calculate`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({ a, b, operation }),
  });

  const data: CalculateResponse | ErrorResponse = await response.json();

  if (!response.ok) {
    throw new Error((data as ErrorResponse).error || 'Calculation failed');
  }

  return (data as CalculateResponse).result;
}
