'use client'
import { useState } from "react"
import { Button, ButtonOutline } from "../components/button"
import { CustomTable } from "../components/table"

export default function App() {
  const [step, setStep] = useState<number>(1)
  const [isAnalysisResult, setIsAnalysisResult] = useState<boolean>(false)

  const techs = [{
    key: "database",
    title: "Database",
  },{
    key: "frontend",
    title: "Front-end",
  },{
    key: "backend",
    title: "Back-end",
  }]

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

  const handleSelectTech = async (tech:string) => {
    setStep(step + 1)
  }

  const handleAnalize = async () => {
    setIsAnalysisResult(true)
  }

  const handleSubmit = async () => {
    console.log("test")
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


  return (
    <div className="bg-background text-text">
      { step ===1 ?
      <div className="container min-h-main flex flex-col justify-center items-center">
        <div className="h-56 text-center">
          <h1 className="text-xl sm:text-3xl font-bold">
            Lorem ipsum dolor sit amet
          </h1>
          <p className="py-4 text-sm sm:text-base">
            consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus.
          </p>
        </div>
        <div className="flex gap-9">
          {techs.map(tech => (
            <div onClick={()=>handleSelectTech(tech.key)} key={tech.key} className="p-8 rounded-xl w-52 text-center bg-secondary hover:bg-primary/70 cursor-pointer">
              {tech.title}
            </div>
          ))}
        </div>
      </div>
      : step === 2 ?
      <div className="container min-h-main flex flex-col justify-center items-center">
        <div className="w-full flex justify-center h-56 ">
          <textarea disabled={isAnalysisResult} id="message" className="w-1/2 h-40 block p-2.5 text-sm text-gray-900 bg-gray-50 rounded-lg outline outline-2 outline-primary" placeholder="Tell us about your project"></textarea>
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
  )
}
