import React, { Component } from 'react';
import TablaNotas from './TablaNotas';

export default class Notas extends Component {
    render() {
        return (
            <div className="py-4">
                <h2>Notas</h2>
                <div className="row">
                    <div className="mb-4 col-lg-12">
                        <div className="mb-4 card card-small">
                            <div className="p-0 px-3 pt-3">
                                <TablaNotas />
                            </div>
                        </div>
                    </div>
                </div>

            </div>
        );
    }
}
