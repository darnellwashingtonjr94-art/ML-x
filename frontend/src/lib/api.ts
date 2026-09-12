const BASE_URL = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000';

export async function runInference(framework: string, data: number[][]) {
  const response = await fetch(`${BASE_URL}/api/v1/predict/${framework}`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({ data }),
  });

  if (!response.ok) {
    throw new Error(`Inference failed: ${response.statusText}`);
  }

  return response.json();
}

