import Image from "next/image";

export default function LandingPage2 () {
  return(
    <div className="">
      <h1 className="text-xl sm:text-3xl font-bold text-center">A beautiful way to share about </h1>
      <h1 className="text-xl sm:text-3xl font-bold text-center">who you are</h1>
      <Image alt="portfolio" src="/images/portfolio.png" width={1200} height={1200} className="w-full my-12 sm:my-20 rounded-lg outline outline-2 outline-primary"/>
    </div>
  )
}