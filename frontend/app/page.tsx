'use client'
import { useEffect, useState } from "react"
import { Button, ButtonOutline } from "@/app/components/button"
import { CustomTable } from "@/app/components/table"
import Step from "@/app/components/Step"
import Loading from "./components/loading"
import { TableResult } from "./components/tableresult"

type TechRes = {
  enable: boolean,
  index: number,
  name: string
}

export default function App() {
  const [step, setStep] = useState<number>(1)
  const [isAnalysisResult, setIsAnalysisResult] = useState<boolean>(false)
  const [techs, setTechs] = useState<TechRes[]>([])
  const [selectedTech, setSelectedTech] = useState<number>(0)
  const [context, setContext] = useState<string>("")
  const [isLoading, setIsLoading] = useState(false)
  const [analysis, setAnalysis] = useState<any>({})
  const [submitAnalysis, setSubmitAnalysis] = useState<any>({})
  const [result, setResult] = useState<any>()

  const steps = [{
    title: "Select Techs",
    description: "",
  },{
    title: "Describe",
    description: "",
  },{
    title: "Review Information",
    description: "",
  }]

  const handleSelectTech = async (index:number) => {
    setStep(step + 1)
    setSelectedTech(index)
  }

  const handleAnalize = async () => {
    setIsAnalysisResult(true)
    sendAnalysis()
  }

  const handleSubmit = async () => {
    setIsLoading(true)
    try {
      const response = await fetch(`${process.env.NEXT_PUBLIC_BACKEND_HOST}/analysis/technology_type/${selectedTech}?k=3`, {
        method: "POST",
        body: JSON.stringify(submitAnalysis),
        headers: {
          "Content-Type": "application/json",
        },
      });
      const data = await response.json();
      setResult(data)
      setIsLoading(false)
    } catch (error) {
      console.log(error)
      setIsLoading(false)
    }
  }

  const fetchTechnologyTypes = async () => {
    try {
      const response = await fetch(
        `${process.env.NEXT_PUBLIC_BACKEND_HOST}/technology_types/`
      );
      const data = await response.json();
      if (data.error) throw new Error(data.error);
      setTechs(data);
    } catch (error) {
      console.log(error)
    }
  }

  useEffect(() => {
    fetchTechnologyTypes()
  }, [])

  useEffect(() => {
    if(isLoading && document !== null) {
      document.getElementById('loading-modal').showModal()
    } else {
      document.getElementById('loading-modal').close()
    }
  }, [isLoading])

  const sendAnalysis = async () => {
    setIsLoading(true)
    try {
      const response = await fetch(`${process.env.NEXT_PUBLIC_BACKEND_HOST}/analysis/technology_type/${selectedTech}`, {
        method: "POST",
        body: JSON.stringify({
          requirement: context,
        }),
        headers: {
          "Content-Type": "application/json",
        },
      });
      const data = await response.json();
      setAnalysis(data)
      setIsLoading(false)
    } catch (error) {
      console.log(error)
      setIsLoading(false)
    }
  }

  return (
    <div className="text-text min-h-main p-4">
      {<Loading />}
      {console.log(submitAnalysis)}
      <div className='grid grid-cols-4 gap-8 p-4 bg-[#F3F6FB] rounded-box min-h-main-component overflow-auto'>
        <div className='h-32 rounded-box bg-[#FFFFFF] col-span-4 p-8 flex justify-center'>
          <Step current={step-1} steps={steps}/>
        </div>
        <div className='rounded-box col-span-4 py-12'>
          { step ===1 ?
          <div className="container flex flex-col justify-center items-center">
            <div className="h-56 text-center">
              <h1 className="text-xl sm:text-3xl font-bold">
                Technology ?
              </h1>
              <p className="py-4 text-sm sm:text-base">
                We will give you the most suitable choice
              </p>
            </div>
            <div className="flex gap-14">
              {techs.map(tech => (
                <button disabled={!tech.enable} onClick={()=> handleSelectTech(tech.index)} key={tech.index} className={`p-8 indicator relative border rounded-xl w-52 text-center ${tech.enable ? 'bg-[#D3E2FD]/70 hover:bg-[#D3E2FD] cursor-pointer': 'bg-[#F2F2F2]'}`}>
                  {!tech.enable &&
                    <span className="indicator-item badge badge-secondary">Coming soon</span>
                  }
                  <div className="m-auto place-items-center">{tech.name}</div>
                </button>
              ))}
            </div>
          </div>
          : step === 2 ?
          <div className="container flex flex-col justify-center items-center">
            <h1 className="text-xl sm:text-2xl font-bold mb-8">
              Tell me more about your project
            </h1>
            <div className="w-full flex justify-center h-56 ">
              <textarea
                value={context}
                onChange={(e)=> setContext(e.target.value)}
                className="w-1/2 h-40 block p-2.5 text-sm text-gray-900 bg-gray-50 rounded-box outline outline-[#80868A] hover:outline-[#202124]"
                placeholder="My project is an IoT project which uses sensors to record the value of outdoor temperature..."/>
            </div>
            {isAnalysisResult ?
              <div className="">
                <CustomTable data={analysis} setSubmitAnalysis={setSubmitAnalysis}/>
                <div className="flex justify-center my-8">
                  <Button text="Submit" onClick={()=> handleSubmit()}/>
                </div>
              </div>
              :
              <ButtonOutline text="Analyze" onClick={()=> handleAnalize()}/>
            }
          </div>
          :
          <div className="container min-h-main flex flex-col justify-center items-center">
            <div className="h-56 text-center">
              <h1 className="text-xl sm:text-3xl font-bold">
                Dingdong !!
              </h1>
            </div>
            <TableResult data={result}/>
          </div>
          }
        </div>
      </div>
    </div>
  )
}
