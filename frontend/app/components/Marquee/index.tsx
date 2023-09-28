"use client"

import Image from "next/image";

const images = ["/icons/gitcoin.svg","/icons/sismo.svg"];

export default function TechWeUse() {
  return(
    <div>
      <h1 className="text-xl sm:text-3xl font-bold text-center mb-16">...with all of the integrations you would expect</h1>
      <div className="flex justify-center gap-16">
        {images.map((image,index) => (
          <Image alt="" width={200} height={200} className="w-12 h-12 sm:w-20 sm:h-20" src={image} key={index}/>
        ))}
      </div>
    </div>
  )
}