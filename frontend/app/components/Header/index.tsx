import Link from 'next/link';

import Wallet from '@/components/Providers/wallet';

export default function Header() {
  return (
    <div className='z-10 p-4 sticky top-0 bg-background'>
      <div className='navbar shadow-xl rounded-box border'>
        <div className='flex-1'>
          <Link href='/' className='btn btn-ghost normal-case text-xl'>
            Home
          </Link>
        </div>
      </div>
    </div>
  );
}