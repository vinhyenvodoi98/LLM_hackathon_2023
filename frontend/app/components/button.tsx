interface ButtonInterface {
  text: string,
  onClick: () => void
}

export const Button = ({text, onClick} :ButtonInterface) => {
  return (
    <button onClick={() => onClick()} className="relative inline-flex items-center justify-center p-4 px-6 py-3 overflow-hidden rounded-lg bg-accent/60 hover:bg-accent shadow-md group">
      <span>{text}</span>
    </button>
  )
}

export const ButtonOutline = ({text, onClick} :ButtonInterface) => {
  return (
    <button onClick={() => onClick()} className="relative inline-flex items-center justify-center p-4 px-6 py-3 overflow-hidden rounded-lg outline outline-1 outline-[#80868A] shadow-md group hover:outline-[#202124]">
      <span>{text}</span>
    </button>
  )
}