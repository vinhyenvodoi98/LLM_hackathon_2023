interface ButtonInterface {
  text: string,
  onClick: () => void
}

export const Button = ({text, onClick} :ButtonInterface) => {
  return (
    <button className="relative inline-flex items-center justify-center p-4 px-6 py-3 overflow-hidden rounded-lg bg-accent shadow-md group">
      <span>{text}</span>
    </button>
  )
}

export const ButtonOutline = ({text, onClick} :ButtonInterface) => {
  return (
    <button className="relative inline-flex items-center justify-center p-4 px-6 py-3 overflow-hidden rounded-lg outline outline-1 shadow-md group">
    <span>{text}</span>
    </button>
  )
}