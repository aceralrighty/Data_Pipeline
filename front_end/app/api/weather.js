import {Pool} from "pg";

const pool = new Pool({
    user: "root",
    host:"localhost",
    database:"weather_db",
    password: "password",
    port: 5432
})
export default async function handler(req, res) {
    try{
        const client = await pool.connect();
        const result = await client.query("SELECT * FROM weather ORDER BY timestamp DESC LIMIT 10")
        client.release();
        return res.json(result)
    } catch(err){
        console.error(err);
        res.status(500).send("Internal Server Error");
    }
}