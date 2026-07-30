"use client";

import { useState } from "react";

type SearchResult = {
  path: string;
  preview: string;
};

export default function Home() {
  const [query, setQuery] = useState("");
  const [results, setResults] = useState<SearchResult[]>([]);
  const [loading, setLoading] = useState(false);

  async function handleSearch() {
    if (!query.trim()) return;
    setLoading(true);
    try {
      const res = await fetch(
        `http://127.0.0.1:8000/search?q=${encodeURIComponent(query)}`
      );
      const data = await res.json();
      setResults(data.results);
    } catch (err) {
      console.error("Search failed:", err);
    } finally {
      setLoading(false);
    }
  }

  return (
    <main className="min-h-screen bg-black text-white p-8">
      <div className="max-w-2xl mx-auto">
        <h1 className="text-3xl font-bold mb-6">DevVault Search</h1>

        <div className="flex gap-2 mb-8">
          <input
            type="text"
            value={query}
            onChange={(e) => setQuery(e.target.value)}
            onKeyDown={(e) => e.key === "Enter" && handleSearch()}
            placeholder="Search your indexed files..."
            className="flex-1 px-4 py-2 rounded bg-gray-800 border border-gray-700 focus:outline-none focus:border-gray-500"
          />
          <button
            onClick={handleSearch}
            className="px-6 py-2 rounded bg-white text-black font-medium hover:bg-gray-200"
          >
            Search
          </button>
        </div>

        {loading && <p className="text-gray-400">Searching...</p>}

        {!loading && results.length === 0 && query && (
          <p className="text-gray-400">No results yet — try a search.</p>
        )}

        <div className="space-y-4">
          {results.map((result, i) => (
            <div key={i} className="border border-gray-800 rounded p-4">
              <p className="text-sm text-gray-400 mb-1">{result.path}</p>
              <p
                className="text-white"
                dangerouslySetInnerHTML={{
                  __html: result.preview
                    .replace(/\[/g, "<mark class='bg-yellow-500 text-black'>")
                    .replace(/\]/g, "</mark>"),
                }}
              />
            </div>
          ))}
        </div>
      </div>
    </main>
  );
}