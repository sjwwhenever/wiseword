import { useState } from "react";
import { Button } from "@/components/ui/button";
import { Textarea } from "@/components/ui/textarea";
import { Loader2 } from "lucide-react";

interface InputSectionProps {
  onConvert: (message: string) => void;
  isLoading: boolean;
}

const InputSection = ({ onConvert, isLoading }: InputSectionProps) => {
  const [message, setMessage] = useState("");

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    if (message.trim()) {
      onConvert(message);
    }
  };

  return (
    <form onSubmit={handleSubmit} className="space-y-4">
      <div className="relative">
        <Textarea
          value={message}
          onChange={(e) => setMessage(e.target.value)}
          placeholder="Enter your scientific message here..."
          className="min-h-[200px] p-4 resize-none text-lg"
          disabled={isLoading}
        />
        <div className="absolute bottom-2 right-2 text-sm text-gray-500">
          {message.length} characters
        </div>
      </div>
      <Button
        type="submit"
        className="w-full sm:w-auto bg-primary hover:bg-secondary text-white font-semibold py-2 px-6 rounded-lg transition-colors"
        disabled={isLoading || !message.trim()}
      >
        {isLoading ? (
          <>
            <Loader2 className="mr-2 h-4 w-4 animate-spin" />
            Converting...
          </>
        ) : (
          "Convert to Campaign"
        )}
      </Button>
    </form>
  );
};

export default InputSection;