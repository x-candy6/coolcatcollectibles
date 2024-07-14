import Container from './Container'

function Card({children}) {
    return ( 
        <Container>
            <div className="  bg-white rounded-xl shadow-md overflow-hidden  card01" style={{ flexGrow: 1 }}>
                {children}
            </div>
        </Container>
     );
}

export default Card;