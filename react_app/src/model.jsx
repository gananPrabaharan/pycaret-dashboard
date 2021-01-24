import React, { useState } from 'react'
import { Container, Form, Row, Col } from 'react-bootstrap'
import { SERVER, getRequestOptions } from './util'
import axios from 'axios'

const Models = (props) => {
    const [state, setState] = useState({
        modelResults: []
    });

    const trainModels = () => {
        const url= SERVER + "trainModels";
        const options = getRequestOptions();
        axios.post(url, options).then((response) => {
            console.info(response)
        });
    }

    return (
        <Container fluid>
            <div style={{margin:"3%"}}>
                <Form method="post" action="trainModels" encType="multipart/form-data">
                    <Form.Group>
                        <Row>
                            <Col sm={1.5}>
                                <Form.Control type="button" value="Train" className="outline-dark center-block"
                                onClick={ trainModels }/>
                            </Col>
                        </Row>
                    </Form.Group>
                </Form>
            </div>
        </Container>
    )
}

export default Models