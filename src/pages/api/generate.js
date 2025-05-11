export const prerender = false;

export async function POST({ request }) {
  const body = await request.json();
  const response = await fetch("http://localhost:8000/generate", {
    method: "POST",
    body: JSON.stringify(body),
    headers: {
      "Content-Type": "application/json",
    },
  });

  const data = await response.json();
  return new Response(JSON.stringify(data), { status: 200 });
}
