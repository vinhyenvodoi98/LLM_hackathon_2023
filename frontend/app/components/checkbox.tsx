interface CheckboxProps {
  checked: boolean;
  name: string
  onChange: (title:string, checked: boolean) => void;
}

const Checkbox: React.FC<CheckboxProps> = ({ checked, name, onChange }) => {
  return (
    <label className="flex items-center space-x-2">
      <input
        type="checkbox"
        className="form-checkbox text-indigo-600 h-5 w-5"
        checked={checked}
        onChange={(e) => onChange(name, e.target.checked)}
      />
    </label>
  );
};

export default Checkbox;
