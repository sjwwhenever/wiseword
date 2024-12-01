import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";

interface OutputSectionProps {
  result: {
    speech: string;
    imageUrl: string;
    videoUrl: string;
  };
}

const OutputSection = ({ result }: OutputSectionProps) => {
  return (
    <div className="space-y-6">
      <Card className="w-full overflow-hidden">
        <CardHeader>
          <CardTitle>Campaign Speech</CardTitle>
        </CardHeader>
        <CardContent>
          <p className="text-lg leading-relaxed">{result.speech}</p>
        </CardContent>
      </Card>

      <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
        <Card>
          <CardHeader>
            <CardTitle>Campaign Image</CardTitle>
          </CardHeader>
          <CardContent>
            <img
              src={result.imageUrl}
              alt="Campaign visual"
              className="w-full h-48 object-cover rounded-lg"
            />
          </CardContent>
        </Card>

        <Card>
          <CardHeader>
            <CardTitle>Campaign Video</CardTitle>
          </CardHeader>
          <CardContent>
            <iframe
              width="100%"
              height="270"
              src={result.videoUrl}
              title="YouTube video player"
              frameBorder="0"
              allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
              allowFullScreen
              className="w-full h-48 object-cover rounded-lg"
            ></iframe>
          </CardContent>
        </Card>
      </div>
    </div>
  );
};

export default OutputSection;