import { Link } from "react-router-dom";
function Footer() {
    return ( 
        <footer class="bg-gray-800 rounded-lg shadow m-4 fixed bottom-0 left-0 right-0 footer">
            <div class="w-full mx-auto max-w-screen-xl p-4 md:flex md:items-center md:justify-between">
                <span class="text-sm text-gray-500 sm:text-center dark:text-gray-400">© 2023 <Link to="/" class="hover:underline">coolcatcollectibles</Link></span>
                <ul class="flex flex-wrap items-center mt-3 text-sm font-medium text-gray-500 dark:text-gray-400 sm:mt-0">
                    <li>
                        <Link to="/about" class="hover:underline me-4 md:me-6">About</Link>
                    </li>
                    <li>
                        <Link to="/register" class="hover:underline me-4 md:me-6">Privacy Policy</Link>
                    </li>
                    <li>
                        <Link to="#" class="hover:underline me-4 md:me-6">Licensing</Link>
                    </li>
                    <li>
                        <Link to="#" class="hover:underline">Contact</Link>
                    </li>
                </ul>
            </div>
        </footer>
     );
}

export default Footer;