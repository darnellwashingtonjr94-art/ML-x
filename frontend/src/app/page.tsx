import InferenceForm from "@/components/InferenceForm";

export default function Home() {
  return (
    <div className="max-w-4xl mx-auto space-y-8">
      <header className="border-b pb-6">
        <h1 className="text-3xl font-bold tracking-tight text-gray-900">ML-x Inference Engine</h1>
        <p className="mt-2 text-sm text-gray-600">
          Select a framework and submit a numerical array to test the multi-model API pipeline.
        </p>
      </header>
      
      <section className="bg-white p-6 rounded-lg shadow-sm border">
        <InferenceForm />
      </section>
    </div>
  );
}
