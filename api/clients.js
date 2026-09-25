export default async function handler(req, res) {
  try {
    if (req.method === 'POST') {
      const { name, phone, service, message = '' } = req.body || {};

      if (!name || !phone || !service) {
        return res.status(400).json({ ok: false, error: 'Missing required fields' });
      }

      const { sql } = await import('@vercel/postgres');

      await sql`
        CREATE TABLE IF NOT EXISTS client_requests (
          id SERIAL PRIMARY KEY,
          name TEXT NOT NULL,
          phone TEXT NOT NULL,
          service TEXT NOT NULL,
          message TEXT,
          created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
        )
      `;

      const result = await sql`
        INSERT INTO client_requests (name, phone, service, message)
        VALUES (${name}, ${phone}, ${service}, ${message})
        RETURNING id, created_at
      `;

      return res.status(200).json({ ok: true, id: result.rows[0]?.id ?? null });
    }

    if (req.method === 'GET') {
      const adminKey = req.headers['x-admin-key'];
      if (!process.env.ADMIN_KEY || adminKey !== process.env.ADMIN_KEY) {
        return res.status(401).json({ ok: false, error: 'Unauthorized' });
      }

      const { sql } = await import('@vercel/postgres');

      await sql`
        CREATE TABLE IF NOT EXISTS client_requests (
          id SERIAL PRIMARY KEY,
          name TEXT NOT NULL,
          phone TEXT NOT NULL,
          service TEXT NOT NULL,
          message TEXT,
          created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
        )
      `;

      const result = await sql`
        SELECT id, name, phone, service, message, created_at
        FROM client_requests
        ORDER BY created_at DESC
        LIMIT 100
      `;

      res.setHeader('Cache-Control', 'no-store');
      return res.status(200).json({ ok: true, requests: result.rows });
    }

    return res.status(405).json({ ok: false, error: 'Method not allowed' });
  } catch (error) {
    console.error(error);
    return res.status(500).json({ ok: false, error: 'Server error' });
  }
}
