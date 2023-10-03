"use client"
import Link from "next/link";
import { Button } from "../button";
import { LandingPageImage } from "./image";

export default function LandingPage1() {
  return (
    <div className="h-screen flex justify-center items-center">
      <div className="md:flex flex-row-reverse">
        <div className="m-auto">
          <LandingPageImage />
        </div>
        <div className="sm:w-[400px] w-[300px] p-4 sm:p-6 flex flex-col justify-around">
          <h1 className="text-xl sm:text-3xl font-bold">
            Lorem ipsum dolor sit amet
          </h1>
          <p className="py-4 text-sm sm:text-base">
            consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus.
          </p>
          <div className="flex gap-4 py-4 justify-center sm:justify-start">
            <Link href="/app">
              <div className="relative inline-flex items-center justify-center p-4 px-6 py-3 overflow-hidden rounded-lg bg-accent/60 hover:bg-accent shadow-md group">
                Start
              </div>
            </Link>
          </div>
        </div>
      </div>
    </div>
  )
}