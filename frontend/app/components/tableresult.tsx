import { useMemo } from "react"

type TableResultProps = {
  data: any
}

export const TableResult = ({data}: TableResultProps) => {

  const titles = useMemo(() => {
    return data.results.map((d:any) => d.database)
  }
  , [data])

  return (
    <div className="overflow-x-auto">
      <table className="table table-zebra">
        <thead>
          <tr>
              <th scope="col" className="px-6 w-64 py-3">
                Objective
              </th>
            {titles.map((title:string, index:number) =>
              <th key={index} scope="col" className="px-6 w-64 py-3">
                {title}
              </th>
            )}
          </tr>
        </thead>
        <tbody>
          {
            Object.keys(data.results[0]).map((objKey:string,index) =>
              <tr key={index}>
                {objKey !== "database" && <td scope="row" className="px-6 py-4 font-medium text-gray-900 dark:text-white">
                  {objKey.split('_').map(word => word.charAt(0).toUpperCase() + word.slice(1).toLowerCase()).join(' ')}
                </td>}
                {titles.map(( v:any ,index: number) =>
                  objKey !== "database" &&
                  <td key={index} scope="row" className="px-6 py-4 font-medium text-gray-900 dark:text-white">
                    {
                      <p className="w-60">{data.results[index][objKey]}</p>
                    }
                  </td>
                )
                }
              </tr>
            )
          }
        </tbody>
      </table>
    </div>
  )
}