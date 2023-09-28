import Image from "next/image"

export default function Feature () {
  return (
    <div>
      <Left/>
      <Right />
    </div>
  )
}

function Left () {
  return(
    <div className="flex justify-center items-center py-16 sm:py-30">
      <div className="md:flex flex-row-reverse">
        <div className="flex justify-center">
          <Image width={200} height={200} alt="github" src="/images/github.jpeg" className="w-[250px] sm:w-[400px] rounded-lg outline outline-2 outline-primary"/>
        </div>
        <div className="sm:w-[400px] w-[300px] p-4 sm:p-6 flex flex-col justify-around">
          <h1 className="text-xl sm:text-3xl font-bold">
            Lorem ipsum dolor sit amet
          </h1>
          <p className="py-4 text-sm sm:text-base">
            consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus.
          </p>
        </div>
      </div>
    </div>
  )
}

function Right () {
  return(
    <div className="flex justify-center items-center py-16 sm:py-30">
      <div className="sm:flex">
        <div className="flex justify-center">
          <Image width={200} height={200} alt="github" src="/images/github.jpeg" className="w-[250px] sm:w-[400px] rounded-lg outline outline-2 outline-primary"/>
        </div>
        <div className="sm:w-[400px] w-[300px] p-4 sm:p-6 flex flex-col justify-around">
          <h1 className="text-xl sm:text-3xl font-bold">
            Lorem ipsum dolor sit amet
          </h1>
          <p className="py-4 text-sm sm:text-base">
            consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus.
          </p>
        </div>
      </div>
    </div>
  )
}