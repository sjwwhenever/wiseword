import ContentConverter from "@/components/ContentConverter";

const Index = () => {
  return (
    <div className="min-h-screen bg-background py-8 px-4 sm:px-6 lg:px-8">
      <div className="max-w-4xl mx-auto">
        <h1 className="text-4xl font-bold text-center mb-8 text-foreground">
          Wise Words
        </h1>
        <ContentConverter />
      </div>
    </div>
  );
};

export default Index;