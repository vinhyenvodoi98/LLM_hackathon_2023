'use client'
import { useEffect, useState } from "react"
import { Button, ButtonOutline } from "@/app/components/button"
import { CustomTable } from "@/app/components/table"
import Step from "@/app/components/Step"

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

  const titles= [{
      key: "name",
      title: "Field name"
    },{
      key: "value",
      title: "Value"
    },{
      key: "consult",
      title: "Consult"
    },{
      key: "explain",
      title: "Explain"
    }]

  const [rows, setRows] = useState([{
      name: "timeSeries",
      value: false,
      consult: "",
      explain: "abc"
    },{
      name: "intensiveDataInsertion",
      value: false,
      consult: "",
      explain: "abc"
    },{
      name: "hugeDataStorage",
      value: false,
      consult: "",
      explain: "abc"
    }])

  const resultTitles= [{
    key: "name",
    title: "Field name"
  },{
    key: "xxxdb",
    title: "xxxDB"
  },{
    key: "aaadb",
    title: "xxxdb"
  }]

  const resultRows= [
    {
      name: "timeSeries",
      xxxdb: "abco",
      aaadb: "abco",
    },{
      name: "intensiveDataInsertion",
      xxxdb: "abco",
      aaadb: "abco",
    },{
      name: "complexQueries",
      xxxdb: "abco",
      aaadb: "abco",
    },{
      name: "hugeDataStorage",
      xxxdb: "abco",
      aaadb: "abco",
    }
  ]

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
    setStep(step + 1)
  }

  const handleCheckbox = (title:string, value:boolean) => {
    const t = rows.map(row => {
      if (row.name === title) {
        return { ...row, value: value };
      }
      return row;
    });
    setRows(t)
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

  const sendAnalysis = async () => {
    const response = await fetch(`${process.env.NEXT_PUBLIC_BACKEND_HOST}/analysis/technology_type/${selectedTech}`, {
      method: "POST",
      body: JSON.stringify({
        context,
      }),
      headers: {
        "Content-Type": "application/json",
      },
    });

    const data = await response.json();
    if (data.error) throw new Error(data.error);
    console.log(data)
  }

  return (
    <div className="text-text">
      <div className='grid grid-cols-4 gap-8 p-4'>
        <div className='rounded-box border col-span-4 p-8 flex justify-center'>
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
            <div className="flex gap-9">
              {techs.map(tech => (
                <button disabled={!tech.enable} onClick={()=> handleSelectTech(tech.index)} key={tech.index} className={`p-8 relative border rounded-xl w-52 text-center ${tech.enable ? 'bg-[#d5e8c5] hover:bg-[#89bd65]/70 cursor-pointer': 'bg-[#CBD5E1]'}`}>
                  {!tech.enable && <div className="bg-[#F77373] rounded-lg absolute top-0 right-0 p-1 text-sm">Coming soon</div>}
                  {tech.name}
                </button>
              ))}
            </div>
          </div>
          : step === 2 ?
          <div className="container flex flex-col justify-center items-center">
            <p className="py-4 text-xl sm:text-base">
              Tell me more about your project
            </p>
            <div className="w-full flex justify-center h-56 ">
              <textarea
                disabled={isAnalysisResult}
                value={context}
                onChange={(e)=> setContext(e.target.value)}
                className="w-1/2 h-40 block p-2.5 text-sm text-gray-900 bg-gray-50 rounded-lg outline outline-2 outline-primary"
                placeholder="My project is an IoT project which uses sensors to record the value of outdoor temperature..."/>
            </div>
            {isAnalysisResult ?
              <div className="">
                <CustomTable titles={titles} rows={rows} onCheckbox={handleCheckbox}/>
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
                Lorem ipsum dolor sit amet
              </h1>
              <p className="py-4 text-sm sm:text-base">
                consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus.
              </p>
            </div>
            <CustomTable titles={resultTitles} rows={resultRows}/>
          </div>
          }
        </div>
      </div>
    </div>
  )
}
