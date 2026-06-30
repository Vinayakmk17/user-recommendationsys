function Hero() {
  return (
    <section className="flex flex-col items-center justify-center h-[85vh] text-center">

      <p className="text-cyan-400 mb-4">
        Hello, I'm
      </p>

      <h1 className="text-7xl font-bold">
        Vinayak
      </h1>

      <h1 className="text-7xl font-bold text-cyan-400">
        Kudlamath
      </h1>

      <p className="mt-6 text-gray-400 max-w-xl">
        Full Stack Developer, Java Programmer and
        AI/ML Enthusiast passionate about building
        modern web applications.
      </p>

      <div className="flex gap-4 mt-8">
        <button className="bg-cyan-500 px-6 py-3 rounded-xl">
          Resume
        </button>

        <button className="border px-6 py-3 rounded-xl">
          Contact
        </button>
      </div>

    </section>
  );
}

export default Hero;