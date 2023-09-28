"use client"

const images = ["/icons/gitcoin.svg","/icons/sismo.svg"];

export default function TechWeUse() {
  return(
    <div>
      <h1 className="text-xl sm:text-3xl font-bold text-center mb-16">…with all of the integrations you'd expect</h1>
      <div className="flex justify-center gap-16">
        {images.map((image,index) => (
          <img className="w-12 h-12 sm:w-20 sm:h-20" src={image} key={index}/>
        ))}
      </div>
    </div>
  )
}