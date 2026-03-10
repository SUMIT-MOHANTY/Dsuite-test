export interface CalculationRequest {
  a: number;
  b: number;
  operation: 'add' | 'subtract' | 'multiply' | 'divide';
}

export interface CalculationResponse {
  result: number;
}

export interface ErrorResponse {
  error: string;
}

export async function calculate(
  a: number,
  b: number,
  operation: string
): Promise<number> {
  const response = await fetch('/api/v1/calculate', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({ a, b, operation }),
  });

  const data = await response.json();

  if (!response.ok) {
    const errorResponse = data as ErrorResponse;
    throw new Error(errorResponse.error || 'An unexpected error occurred');
  }

  const successResponse = data as CalculationResponse;
  return successResponse.result;
}
