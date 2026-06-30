function Navbar() {
  return (
    <nav className="flex justify-between items-center px-10 py-6">
      <h1 className="text-2xl font-bold text-cyan-400">
        Vinayak.
      </h1>

      <ul className="flex gap-8 text-gray-300">
        <li>About</li>
        <li>Skills</li>
        <li>Projects</li>
        <li>Contact</li>
      </ul>
    </nav>
  );
}

export default Navbar;