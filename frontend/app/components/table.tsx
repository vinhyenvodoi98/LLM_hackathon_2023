import { Dispatch, useEffect, useMemo } from "react";
import Select from 'react-select';

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
    "Explanation",
    "Question",
    "Select value"
  ]
  return (
    <div className="overflow-x-auto">
      <table className="table table-zebra">
        <thead>
          <tr>
            {titles.map((title, index) =>
              <th key={index} scope="col" className="px-6 py-3">
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
                    <td key={index} rowSpan={Object.keys(data[key]).length} scope="row" className="px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white">
                      {key.split('_').map(word => word.charAt(0).toUpperCase() + word.slice(1).toLowerCase()).join(' ')}
                    </td>
                  }
                  {
                    Object.keys(data[key][objectKey]).map((row, index) =>
                    <td key={index} scope="row" className="px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white">
                      {
                        row === "value" ?
                          <Selector value={data[key][objectKey][row]} objkey={objectKey} setSubmitAnalysis={setSubmitAnalysis}/>
                        : data[key][objectKey][row]
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