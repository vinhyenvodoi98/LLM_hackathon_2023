import Checkbox from "./checkbox"
import { ChatIcon } from "./Icon";
import Tooltip from "./tooltip";

type CustomTableProps = {
  titles: {
    key: string,
    title: string,
  }[],
  rows: Record<string, any>[]
  onCheckbox?: (title:string, value:boolean) => void;
}

export const CustomTable = ({titles, rows, onCheckbox}: CustomTableProps) => {

  return (
    <div className="overflow-x-auto">
      <table className="table table-zebra">
        <thead>
          <tr>
            {titles.map(title =>
              <th key={title.key} scope="col" className="px-6 py-3">
                {title.title}
              </th>
            )}
          </tr>
        </thead>
        <tbody>
          {rows.map((row,index) =>
            <tr key={index} className="bg-white dark:bg-gray-800 dark:border-gray-700">
                {titles.map(title =>
                  <td key={title.key} scope="row" className="px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white">
                    {title.key === "value" ?
                      onCheckbox && <Checkbox checked={row[title.key]} name={row.name} onChange={onCheckbox} />
                      : title.key === "explain" ?
                      <Tooltip text={row[title.key]}/>
                      : title.key === "consult" ?
                      <ChatIcon/>
                      :
                      row[title.key]
                    }
                  </td>
                )}
            </tr>
            )}
        </tbody>
      </table>
    </div>
  )
}