type TableResultProps = {
  data: any
}

export const TableResult = ({data}: TableResultProps) => {
  const titles = [
    "Commercial",
    "Data Type",
    "Database",
    "Maturity",
    "Open Source",
    "Read Consistency",
    "Respond Time",
    "Volume",
    "Website"
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
            data.results.map((data:any, index:number) =>
              <tr key={index} className="">
                {
                  Object.keys(data).map((ObjKey, index) =>
                  <td key={index} scope="row" className="px-6 py-4 font-medium text-gray-900 dark:text-white">
                    {
                      <p className="w-60">{data[ObjKey]}</p>
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