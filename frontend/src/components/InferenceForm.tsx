"use client";

import { useState } from "react";
import { runInference } from "@/lib/api";
import ResultCard from "./ResultCard";

export default function InferenceForm() {
  const [framework, setFramework] = useState("pytorch");
  const [inputData, setInputData] = useState("[[1.0, 2.0, 3.0]]");
  const [result, setResult] = useState<any>(null);
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setLoading(true);
    try {
      const parsedData = JSON.parse(inputData);
      const res = await runInference(framework, parsedData);
      setResult(res);
    } catch (error: any) {
      setResult({ error: error.message || "Invalid JSON array" });
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
      <form onSubmit={handleSubmit} className="space-y-4">
        <div>
          <label className="block text-sm font-medium text-gray-700">Framework</label>
          <select 
            value={framework} 
            onChange={(e) => setFramework(e.target.value)}
            className="mt-1 block w-full rounded-md border-gray-300 shadow-sm p-2 border"
          >
            <option value="pytorch">PyTorch</option>
            <option value="tensorflow">TensorFlow</option>
            <option value="xgboost">XGBoost</option>
          </select>
        </div>
        <div>
          <label className="block text-sm font-medium text-gray-700">Input Data (JSON 2D Array)</label>
          <textarea 
            value={inputData}
            onChange={(e) => setInputData(e.target.value)}
            rows={4}
            className="mt-1 block w-full rounded-md border-gray-300 shadow-sm p-2 border font-mono text-sm"
          />
        </div>
        <button 
          type="submit" 
          disabled={loading}
          className="bg-blue-600 text-white px-4 py-2 rounded-md hover:bg-blue-700 disabled:opacity-50"
        >
          {loading ? "Running..." : "Run Inference"}
        </button>
      </form>
      
      <div>
        <h3 className="text-sm font-medium text-gray-700 mb-2">Output</h3>
        <ResultCard data={result} />
      </div>
    </div>
  );
}
