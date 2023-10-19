import { Dispatch, useEffect, useMemo } from "react";
import Select from 'react-select';
import ContentWithLineBreaks from "./contentbreak";

type CustomTableProps = {
  data: any
  setSubmitAnalysis: Dispatch<any>
}

const Selector = ({value, objkey, setSubmitAnalysis}:{value: any, objkey: string, setSubmitAnalysis: Dispatch<any>}) => {
  const options = value.selectable_value.map((v:any) => ({label:v.toString(), value:v }))
  const defaultValue = value.multi_select ? value.current.map((v:any) => ({label:v.toString(), value:v })) : {label: value.current?.toString(), value: value.current }
  const handleChange = (objkey:string, value:any) => {
    if (typeof value.length === "number"){
      const newValue = value.map((v:any) => v.value)
      setSubmitAnalysis((prevSettings:any) => {
        return { ...prevSettings, [objkey]: newValue };
      });
    }
    else {
      setSubmitAnalysis((prevSettings:any) => {
        return { ...prevSettings, [objkey]: value.value };
      });
    }
  };

  useEffect(() => {
    setSubmitAnalysis((prevSettings:any) => {
      return { ...prevSettings, [objkey]: value.current };
    });
  }, [])

  return (
    <Select
      className="basic-single w-60"
      classNamePrefix="select"
      isMulti={value.multi_select}
      defaultValue={defaultValue}
      options={options}
      onChange={(e)=> handleChange(objkey, e)}
    />
  )
}

export const CustomTable = ({data, setSubmitAnalysis}: CustomTableProps) => {
  const titles = [
    "Objective",
    "Question",
    "Explanation",
    "Select value"
  ]

  return (
    <div className="overflow-x-auto">
      <table className="table table-zebra">
        <thead>
          <tr>
            {titles.map((title, index) =>
              <th key={index} scope="col" className="px-6 w-64 py-3">
                {title}
              </th>
            )}
          </tr>
        </thead>
        <tbody>
          {
            Object.keys(data).map((key) =>
              Object.keys(data[key]).map((objectKey, index) =>
                <tr key={index} className="">
                  {
                  index===0 &&
                    <td key={index} rowSpan={Object.keys(data[key]).length} scope="row" className="px-6 py-4 font-medium text-gray-900 dark:text-white">
                      {key.split('_').map(word => word.charAt(0).toUpperCase() + word.slice(1).toLowerCase()).join(' ')}
                    </td>
                  }
                  {
                    Object.keys(data[key][objectKey]).map((row, index) =>
                    <td key={index} scope="row" className="px-6 py-4 font-medium text-gray-900 dark:text-white">
                      {
                        row === "value" ?
                          <Selector value={data[key][objectKey][row]} objkey={objectKey} setSubmitAnalysis={setSubmitAnalysis}/>
                        : row === "explanation" ?
                        <div className="dropdown dropdown-end">
                          <label tabIndex={0} className="btn btn-circle btn-ghost btn-xs text-info">
                            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" className="w-4 h-4 stroke-current"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>
                          </label>
                          <div tabIndex={0} className="card compact dropdown-content z-[1] shadow bg-base-100 rounded-box w-64">
                            <div className="card-body">
                              <ContentWithLineBreaks content={data[key][objectKey][row]}/>
                            </div>
                          </div>
                        </div>
                        :
                        <p className="w-60">{data[key][objectKey][row]}</p>
                      }
                    </td>
                  )}
                </tr>
              )
            )
          }
        </tbody>
      </table>
    </div>
  )
}