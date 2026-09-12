export default function ResultCard({ data }: { data: any }) {
  if (!data) {
    return (
      <div className="h-full min-h-[150px] bg-gray-50 border border-dashed rounded-md flex items-center justify-center text-gray-400 text-sm">
        Awaiting input...
      </div>
    );
  }

  return (
    <div className="bg-gray-900 text-green-400 p-4 rounded-md overflow-x-auto min-h-[150px]">
      <pre className="text-sm font-mono whitespace-pre-wrap">
        {JSON.stringify(data, null, 2)}
      </pre>
    </div>
  );
}
