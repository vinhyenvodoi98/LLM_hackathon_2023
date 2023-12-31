import Link from 'next/link';

export default function Header() {
  return (
    <div className='z-10 p-4 sticky top-0 bg-background'>
      <div className='navbar shadow-xl rounded-box border border-[#80868A]'>
        <div className='flex-1'>
          <Link href='/' className='btn btn-ghost normal-case text-xl'>
            Home
          </Link>
        </div>
      </div>
    </div>
  );
}