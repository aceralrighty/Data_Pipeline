import useSWR from "swr"

const fetcher = (url) => fetch(url).then((res) => res.json());
export default function Home() {
    const {data, error} = useSWR("/api/weather", fetcher, {refreshInterval: 60000});

    if (error) return <div>Error loading data</div>;
    if (!data) return <div>Loading...</div>;
    return (
        <div>
            <h1>Latest Weather Data</h1>
            <ul>
                {data.map((entry) => (
                    <li key={entry.id}>
                        {entry.city}: {entry.temperature.toFixed(1)}°C, {entry.humidity}% humidity
                        ({new Date(entry.timestamp).toLocaleString()})
                    </li>
                ))}
            </ul>
        </div>
    );

}
