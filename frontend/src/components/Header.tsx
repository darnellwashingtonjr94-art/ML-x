import Link from "next/link";

export default function Header() {
  return (
    <header className="bg-gray-900 border-b border-gray-800 text-white py-4 px-6 mb-8 rounded-lg shadow-md mt-4">
      <div className="flex items-center justify-between">
        <div className="flex items-center gap-2">
          <div className="w-8 h-8 bg-blue-500 rounded-md flex items-center justify-center font-bold">
            M
          </div>
          <span className="text-xl font-semibold tracking-wide">ML-x Platform</span>
        </div>
        <nav className="space-x-4 text-sm font-medium text-gray-300">
          <Link href="/" className="hover:text-white transition-colors">Dashboard</Link>
          <Link href="/docs" className="hover:text-white transition-colors">API Specs</Link>
        </nav>
      </div>
    </header>
  );
}
