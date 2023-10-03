import Link from "next/link"

export default function Header() {
  return (
    <header className='sticky top-0 z-50 bg-background border-b'>
      <div className='container flex h-14 items-center justify-between'>
        <Link href="/">Home</Link>
      </div>
    </header>
  );
}
