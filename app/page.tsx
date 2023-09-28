import Feature from "./components/Feature";
import LandingPage1 from "./components/LandingPage1";
import LandingPage2 from "./components/LandingPage2";
import TechWeUse from "./components/Marquee";
import UserRank from "./components/UserRank";

export default function Home() {
  return (
    <div className="bg-background text-text">
      <div className="container">
        <LandingPage1 />
        <LandingPage2 />
        <UserRank />
        <TechWeUse />
        <Feature />
      </div>
    </div>
  )
}
