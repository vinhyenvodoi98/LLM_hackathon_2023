import { useState } from "react";
import { TooltipIcon } from "./icon";

interface TooltipProps {
  text: string;
}

const Tooltip: React.FC<TooltipProps> = ({ text }) => {
  const [isTooltipVisible, setIsTooltipVisible] = useState(false);

  return (
    <div className="relative inline-block">
      <div
        className="text-blue-600 cursor-pointer"
        onMouseEnter={() => setIsTooltipVisible(true)}
        onMouseLeave={() => setIsTooltipVisible(false)}
      ><TooltipIcon/></div>
      {isTooltipVisible && (
        <div className="bg-secondary border border-blue-600 text-blue-600 text-xs rounded-lg p-2 absolute bottom-6 left-6 z-10">
          {text}
        </div>
      )}
    </div>
  );
};

export default Tooltip;