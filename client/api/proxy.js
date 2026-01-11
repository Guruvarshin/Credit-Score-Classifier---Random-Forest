export default async function handler(req, res) {
    const backendIP = "13.50.231.193";
    const targetUrl = `http://${backendIP}${req.url.replace('/api/proxy', '')}`;

    try {
        const options = {
            method: req.method,
            headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
        };

        if (req.method === 'POST') {
            options.body = new URLSearchParams(req.body).toString();
        }

        const response = await fetch(targetUrl, options);
        const data = await response.json();
        res.status(200).json(data);
    } catch (e) {
        res.status(500).json({ error: "Bridge Error: " + e.message });
    }
}