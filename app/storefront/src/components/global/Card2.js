import Container2 from './Container2'

function Card2({children}) {
    return ( 
        <Container2>
            <div className="  bg-white rounded-xl shadow-md overflow-hidden  card01" style={{ flexGrow: 1 }}>
                {children}
            </div>
        </Container2>
     );
}

export default Card2;