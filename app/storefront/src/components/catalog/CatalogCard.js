import Container from "../global/Container";

function CatalogCard({children}) {
    return ( 
        <Container>
            <div className="catalog-card bg-white rounded-xl shadow-md overflow-hidden p-4" style={{ flex: '1 1 100%', maxWidth: '100%' }}>
                {children}
            </div>
        </Container>
     );
}

export default CatalogCard;